use std::{convert::Infallible, rc::Rc};

use hyper::{Body, HeaderMap, Response, StatusCode};
use mysql::prelude::Queryable;
use serde::Serialize;

use crate::{get_table, response_with_status_code};

#[derive(Serialize)]
struct SQLEntry {
    created_at: String,
    celsius: f64,
    humidity: f64,
}

fn get_date_part(parts: &Vec<(Rc<String>, Rc<String>)>) -> Option<Rc<String>> {
    for part in parts {
        if &*part.0 == "since-date" {
            return Some(part.1.clone());
        }
    }
    None
}

fn should_return_last_val(parts: &Vec<(Rc<String>, Rc<String>)>) -> bool {
    for part in parts.iter() {
        if &*part.0 == "get_last" {
            return &*part.1 == "true";
        }
    }
    return false;
}

pub fn select_data(
    parts: &Vec<(Rc<String>, Rc<String>)>,
    headers: &HeaderMap,
    mysql_conn: &mut mysql::Conn,
    database_id: usize,
) -> Result<Response<Body>, Infallible> {
    if should_return_last_val(parts) {
        return send_last_element(mysql_conn, database_id);
    }

    // Get date from argument
    let date = if let Some(date) = get_date_part(parts) {
        date
    }
    // It might be sent as a header, so check that
    else if headers.contains_key("x-since-date") {
        match headers["x-since-date"].to_str() {
            Ok(k) => Rc::new(k.to_string()),
            Err(e) => {
                // The user have screwed up and sent something really strange
                return response_with_status_code(e.to_string(), StatusCode::BAD_REQUEST);
            }
        }
    }
    // No date is sent, and we weren't supposed to send the last item, user screwed up
    else {
        return response_with_status_code("No date", StatusCode::BAD_REQUEST);
    };

    let query: Vec<(String, String, String)> = match mysql_conn.query(format!(
        "SELECT created_at, celsius, humidity FROM {} WHERE created_at > '{}'",
        get_table(database_id),
        date
    )) {
        Ok(k) => k,
        Err(e) => {
            return response_with_status_code(format!("{:?}", e), StatusCode::INTERNAL_SERVER_ERROR)
        }
    };

    let mut entries: Vec<SQLEntry> = Vec::new();
    for (date, cel, hum) in query.into_iter() {
        // Parse into floats
        let (cel, hum) = (cel.trim().parse::<f64>(), hum.trim().parse::<f64>());

        // Reslove possible parseerror where the databse is broken
        let (celsius, humidity): (f64, f64) = if let (Ok(cel), Ok(hum)) = (cel, hum) {
            (cel, hum)
        } else {
            // We got weird values, which aren't floats
            return response_with_status_code(
                "The database is somehow broken, values of celsius and/or humidity are'nt floats",
                StatusCode::INTERNAL_SERVER_ERROR,
            );
        };

        entries.push(SQLEntry {
            created_at: date,
            celsius,
            humidity,
        })
    }

    // Shouldn't be possible to fail here, but anyways, good meassure to keep down unwraps
    match serde_json::to_string(&entries) {
        Ok(k) => Ok(Response::new(k.into())),
        Err(e) => response_with_status_code(e.to_string(), StatusCode::INTERNAL_SERVER_ERROR),
    }
}

fn send_last_element(
    mysql_conn: &mut mysql::Conn,
    database_id: usize,
) -> Result<Response<Body>, Infallible> {
    let mut response_from_sqlserver: Vec<(String, String, String)> =
        match mysql_conn.query(format!(
            "SELECT created_at, celsius, humidity FROM {0} WHERE id=(SELECT max(id) FROM {0})",
            get_table(database_id)
        )) {
            Ok(k) => k,
            Err(e) => return Ok(Response::new(format!("{:?}", e).into())),
        };

    if response_from_sqlserver.len() != 1 {
        return response_with_status_code(
            "There are more than one entry with the same id",
            StatusCode::INTERNAL_SERVER_ERROR,
        );
    }
    // Move the entry out of the vector so that we dont have to unnecessarily copy
    let downloaded_entry = response_from_sqlserver.remove(0);

    let decoded_entry = SQLEntry {
        created_at: downloaded_entry.0,
        celsius: downloaded_entry
            .1
            .trim()
            .parse()
            .expect("Kunde inte parsea celsius"),
        humidity: downloaded_entry
            .2
            .trim()
            .parse()
            .expect("Kunde inte parsea humidity"),
    };

    match serde_json::to_string(&decoded_entry) {
        Ok(k) => Ok(Response::new(k.into())),
        Err(e) => response_with_status_code(e.to_string(), StatusCode::INTERNAL_SERVER_ERROR),
    }
}

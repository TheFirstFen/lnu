use std::convert::Infallible;

use hyper::{Body, HeaderMap, Response, StatusCode};
use mysql::{params, prelude::Queryable};

use crate::{get_table, response_with_status_code};

pub fn insert_data(
    headers: &HeaderMap,
    mysql_conn: &mut mysql::Conn,
    database_id: usize,
) -> Result<Response<Body>, Infallible> {
    // Get celsius and humidity from headers
    let (celsius, humidity) =
        if let (Some(cel), Some(hum)) = (headers.get("x-celsius"), headers.get("x-humidity")) {
            // Try to convert the params to &str, and if not possible send error to user
            if let (Ok(cel), Ok(hum)) = (cel.to_str(), hum.to_str()) {
                (cel, hum)
            } else {
                return response_with_status_code("Invalid data", StatusCode::BAD_REQUEST);
            }
        } else {
            // All data is not sent to us!
            return response_with_status_code("No data!", StatusCode::BAD_REQUEST);
        };

    // Check if celsius paramter is a float/int
    if celsius.trim().parse::<f64>().is_err() {
        return response_with_status_code(
            "The celsius parameter isn't a float or integer",
            StatusCode::BAD_REQUEST,
        );
    }

    // Check if humidity paramter is a float/int
    if humidity.trim().parse::<f64>().is_err() {
        return response_with_status_code(
            "The humidity parameter isn't a float or integer",
            StatusCode::BAD_REQUEST,
        );
    }

    if let Err(e) = mysql_conn.exec_drop(
        format!(
            r"INSERT INTO {} (celsius, humidity) VALUES (:celsius, :humidity)",
            get_table(database_id) // Got error when I tried to insert it with params!
        ),
        params! {
            "celsius"=>celsius,
            "humidity"=>humidity,
        },
    ) {
        eprintln!("{:?}", &e);
        return response_with_status_code(e.to_string(), StatusCode::BAD_REQUEST);
    } else {
        return Ok(Response::new("Item added".into()));
    }
}

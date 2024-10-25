use hyper::{Body, Method, Request, Response, StatusCode};
use std::{convert::Infallible, fmt::Display, rc::Rc};
use user::User;

mod insert;
mod select;
mod user;

use insert::insert_data;
use select::select_data;

const SQL_PASSWORD: &'static str = "JA4eRQhwizvMB69VA2UgXu5iP9KsgatvsCxnExjyBy3em";
const SQL_USERNAME: &'static str = "sensor_one";
const SQL_HOST: &'static str = "billenius.com";
const SQL_DATABASE: &'static str = "termoster";
const SQL_PORT: u16 = 3306;

fn response_with_status_code<T: Into<Body>>(
    body: T,
    status_code: StatusCode,
) -> Result<Response<Body>, Infallible> {
    let mut response = Response::new(body.into());
    *response.status_mut() = status_code;
    Ok(response)
}

fn query_to_parts(query: &str) -> Vec<(Rc<String>, Rc<String>)> {
    let normalized_str = query.replace("?", "\u{2122}").replace("&", "\u{2122}");
    normalized_str
        .split("\u{2122}")
        .map(|pair| {
            let mut p = pair.split("=");
            (
                Rc::new(p.next().unwrap().to_string()),
                Rc::new(p.next().unwrap().to_string()),
            )
        })
        .collect::<Vec<(Rc<String>, Rc<String>)>>()
}

pub async fn handle(req: Request<Body>) -> Result<Response<Body>, Infallible> {
    let sql_url = format!(
        "mysql://{}:{}@{}:{}/{}",
        &SQL_USERNAME, &SQL_PASSWORD, &SQL_HOST, &SQL_PORT, &SQL_DATABASE
    );

    let mut mysql_conn = match mysql::Conn::new(sql_url.as_str()) {
        Ok(k) => k,
        Err(e) => {
            // The SQL server is probably down
            return response_with_status_code(e.to_string(), StatusCode::INTERNAL_SERVER_ERROR);
        }
    };

    let parts = if let Some(query) = req.uri().query() {
        Some(query_to_parts(query))
    } else {
        None
    };

    let user = match get_user(&req, &parts) {
        Ok(user) => user,
        Err(error) => return error,
    };

    // Try to get the database id for this user
    let database_id = match user.get_id_from_db(&mut mysql_conn) {
        Ok(id) => id,
        Err(error_to_send) => {
            return error_to_send;
        }
    };

    if req.method() == Method::GET {
        let parts = &parts.expect("Parts finns inte!!!");
        if should_verify(parts) {
            response_with_status_code("valid user", StatusCode::OK)
        } else {
            select_data(parts, req.headers(), &mut mysql_conn, database_id)
        }
    } else if req.method() == Method::POST {
        insert_data(req.headers(), &mut mysql_conn, database_id)
    } else {
        response_with_status_code(
            "Not a GET nor a POST request",
            StatusCode::METHOD_NOT_ALLOWED,
        )
    }
}

fn should_verify(parts: &Vec<(Rc<String>, Rc<String>)>) -> bool {
    for part in parts {
        if &*part.0 == "verify" {
            return &*part.1 == "true";
        }
    }
    false
}

fn get_user(
    req: &Request<Body>,
    parts: &Option<Vec<(Rc<String>, Rc<String>)>>,
) -> Result<User, Result<Response<Body>, Infallible>> {
    // Get user from headers or argument depending of method
    let user = if req.method() == Method::POST {
        // This is from the sensor which sends in custom headers
        User::from_headers(req.headers())
    } else if req.method() == Method::GET {
        if let Some(parts) = parts {
            // In the case that we actually got the arguments
            User::from_arg(parts)
        } else {
            // They might fuck up and not send anything, reply with error
            return Err(response_with_status_code(
                "Inga argument",
                StatusCode::BAD_REQUEST,
            ));
        }
    } else {
        // They might use a method that isn't allowed/handeled
        return Err(response_with_status_code(
            "Otillåtna headers",
            StatusCode::METHOD_NOT_ALLOWED,
        ));
    };

    if let Some(user) = user {
        // Now get the user struct, in the case that we actually got the correct username/password
        Ok(user)
    } else {
        // They sent the wrong username/password
        Err(response_with_status_code(
            "Inget användarnamn/lösenord matchar",
            StatusCode::FORBIDDEN,
        ))
    }
}

fn get_table(database_id: usize)  -> String{
    if database_id == 1 {
        "meassures".to_string()
    } else {
        format!("user_{}", database_id)
    }
}

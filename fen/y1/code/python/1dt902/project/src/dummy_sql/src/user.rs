use std::{convert::Infallible, rc::Rc};

use base64::encode;
use hyper::{Body, HeaderMap, Response, StatusCode};
use mysql::{params, prelude::Queryable};

use crate::response_with_status_code;

#[derive(Debug)]
pub struct User {
    username: Rc<String>,
    password: String,
}

impl User {
    pub fn from_arg(parts: &Vec<(Rc<String>, Rc<String>)>) -> Option<Self> {
        let (mut username, mut pass): (Option<Rc<String>>, Option<String>) = (None, None);

        for part in parts {
            if *part.0 == "username" {
                username = Some(part.1.clone());
            } else if *part.0 == "password" {
                let encoded_password = encode(part.1.as_bytes());
                pass = Some(encoded_password);
            }
        }

        if let (Some(username), Some(password)) = (username, pass) {
            Some(Self { username, password })
        } else {
            None
        }
    }

    pub fn from_headers(headers: &HeaderMap) -> Option<Self> {
        if let (Some(username), Some(password)) =
            (headers.get("x-username"), headers.get("x-password"))
        {
            let encoded_password = encode(password.to_str().ok()?.to_string().as_bytes());
            Some(Self {
                username: Rc::new(username.to_str().ok()?.to_string()),
                password: encoded_password,
            })
        } else {
            None
        }
    }

    pub fn get_id_from_db(
        &self,
        mysql_conn: &mut mysql::Conn,
    ) -> Result<usize, Result<Response<Body>, Infallible>> {
        let query = "SELECT id FROM users WHERE username = :username AND password = :password";

        let stmt = match mysql_conn.prep(query) {
            Ok(k) => k,
            Err(e) => {
                return Err(response_with_status_code(
                    e.to_string(),
                    StatusCode::INTERNAL_SERVER_ERROR,
                ));
            }
        };

        let mut response: Vec<usize> = match mysql_conn.exec(
            stmt,
            params! {"username"=>&*self.username,"password"=> &self.password},
        ) {
            Ok(k) => k,
            Err(e) => {
                return Err(response_with_status_code(
                    e.to_string(),
                    StatusCode::INTERNAL_SERVER_ERROR,
                ))
            }
        };

        if response.len() != 1 {
            return Err(response_with_status_code(
                "Ingen användare matchar",
                StatusCode::FORBIDDEN,
            ));
        } else if response.len() > 1 {
            return Err(response_with_status_code(
                "Flera användare matchar",
                StatusCode::INTERNAL_SERVER_ERROR,
            ));
        }
        Ok(response.remove(0))
    }
}

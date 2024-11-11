use dummy_sql::handle;
use hyper::service::{make_service_fn, service_fn};
use hyper::Server;
use local_ip_address::local_ip;
use std::convert::Infallible;
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    // mysql

    // We'll bind to 127.0.0.1:3000
    let addr = SocketAddr::from(([0, 0, 0, 0], 8579));

    // A `Service` is needed for every connection, so this
    // creates one from our `hello_world` function.
    let make_svc = make_service_fn(|_conn| async {
        // service_fn converts our function into a `Service`
        Ok::<_, Infallible>(service_fn(handle))
    });

    let server = Server::bind(&addr).serve(make_svc);

    // Get local ip, if possible or else nevermind
    let local_ip_address = local_ip()
        .and_then(|ipaddr| Ok(ipaddr.to_string()))
        .unwrap_or_default();
    println!(
        "Listening on port {} (local ip: {})",
        addr.port(),
        local_ip_address
    );

    // Run this server for... forever!
    if let Err(e) = server.await {
        eprintln!("server error: {}", e);
    }
}

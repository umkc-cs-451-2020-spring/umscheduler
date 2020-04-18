#[macro_use]
extern crate rouille;

use rouille::{
    Request,
    Response,
};

fn main() {
    rouille::start_server("localhost:8080", move |req| {
        // A simple test
        router!(req,
            (GET) (/) => {
                Response::text("Hello! Unfortunately there is nothing to see here.")
            },
            _ => Response::empty_404()
        )
    });
}

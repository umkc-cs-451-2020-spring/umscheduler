<h1 align="center">UMScheduler</h1>
<div align="center">
  <strong>
    A course scheduling application for the UM system.
  </strong>
</div>

<br />

## Installation

```sh
cd umscheduler
cargo build --release
```

## Members and Contributors

```md
Samuel Lim
Zach Zoltek
Alivia Dutcher
Yazdan Riazi
```

## Problem

The prompt we have chosen is course scheduling, under the supervision of Gina Campbell.

## Documentation

### Internal

Files concerning group discussion, meetings, iterations and more can be found under the `documentation` folder.

### Usage

Automated documentation sourced from source comments and function signatures can tentatively be found within the automated docs.

To source these documents, first build them with the following command:

```sh
cargo doc --release --no-deps
```

### Setting up the database

If you are running the UMScheduler you will need to have a local instance of MySQL Server running with the proper database setup. For this you will need [MySQL Workbench](https://www.mysql.com/products/workbench/). 

* Download and install the workbench and follow the setup procedure. Once you are finished you should have a local instance of MySQL server running and an open workbench.
* Make sure you are connected to the database. To ensure that you are head to Server > Startup/Shutdown and make sure you see "The database server instance is running"
  * If the server is not running, hit "Start Server"
* After ensuring you are connected, go to File > Open SQL Script and open `semester-project-group-14/database/DBSchema.sql`
* Run the SQL file in its entirety. There should be no errors.
* Go into your "Schemas" panel on the left (if there is no "Schemas" panel, go to View > Panels > Show Sidebar), right click and hit "Refresh all"
* There should be a schema named "umschedulerschema"

### Running the frontend

To setup and run the frontend you'll need the follow prerequisites:

* Node v13.13.0+
* npm v6.14.4

Run the following commands from the `ui/` folder:

  1. `npm install`
  2. `npm run build`
  3. `npm start`

Then navigate to `http://localhost:3000` and you should see a local instance of the frontend running in your browser!

### Running the backend

Of course, for full functionality you'll need to be have a running backend along with your frontend. To accomplish this ensure you have the latest version of Rust installed and perform the following:

  1. Navigate to `umscheduler/`
  2. Run `cargo run`

The build should complete with no errors and you should have a backend running on `http://localhost:8080`

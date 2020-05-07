/// Begins the automated connection into the database endpoints.

use std::cmp::Eq;
use sqlx::encode::Encode;
use sqlx::decode::Decode;


/// Subject to change: the type alias for ID values is based on the intrinsic database used. (i.e. MySQL)
type ID = u32;

/// Accessor is for derive use by the server,
/// defining the u8 value taken from the database at ProfileAccess. 
#[repr(u8)]
enum Accessor {
    /// These are anonymous viewers or people who have access without an account.
    Unregistered = 0b00,
    /// Profiles with limited share access.
    Normal = 0b01,
    /// Those with full edit permissions to the profile information or associated schedules.
    Admin = 0b10,
}

impl Into<u8> for Accessor {
    fn into(self: Self) -> u8 { self as u8 }
}

#[derive(PartialEq, Eq, Encode, Decode)]
struct Profile {
    username: String,
    handle: String,
    profile_id: ID,
}

#[derive(PartialEq, Eq, Encode, Decode)]
struct ProfileAccess {
    profile_id: ID,
    access_value: u8,
}

#[derive(PartialEq, Eq, Encode, Decode)]
struct ProfileSchedule {
    profile_id: ID,
    schedule_id: ID,
    shareable: bool,
}

#[derive(PartialEq, Eq, Encode, Decode)]
struct Schedule {
    schedule_id: ID,
    // timetable: Vec<ID>,
}

#[derive(PartialEq, Eq, Encode, Decode)]
struct SavedProfile {
    profile: Profile,
}
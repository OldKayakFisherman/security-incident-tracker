from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    email: str
    password: str
    is_active: bool
    is_admin: bool


@dataclass
class IncidentEntity:
    id: int
    external_case_number: str
    ip: str
    pen_tester: bool
    region: str
    country: str
    description: str
    script_injection: bool
    command_injection: bool
    sql_injection: bool
    cross_frame_scripting: bool
    path_discovery: bool
    cross_site_request_forgery: bool
    other: bool

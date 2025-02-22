use std::fmt;

#[derive(Debug, PartialEq, Eq)]
pub struct Clock {
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let total_minutes = hours * 60 + minutes;
        Self::normalize(total_minutes)        
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Self::normalize(self.minutes + minutes)
    }

    fn normalize(minutes: i32) -> Self {
        let total_minutes = (minutes % 1440 + 1440) % 1440;
        Clock { minutes: total_minutes }
    }

    fn hours(&self) -> i32 {
        self.minutes / 60
    }

    fn minutes(&self) -> i32 {
        self.minutes % 60
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours(), self.minutes())
    }
}
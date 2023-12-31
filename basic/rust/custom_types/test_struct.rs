fn a() {
    // do something
}

fn b() {
    // do something
}

struct Test {
    a: fn(),
    b: fn(),
}

fn main() {
    let test = Test { a, b };
    (test.a)();
    loop {}
}
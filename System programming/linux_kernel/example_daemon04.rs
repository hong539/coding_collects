use daemonize::Daemonize;

fn main() {
    let stdout = std::fs::File::create("/tmp/stdout.log").unwrap();
    let stderr = std::fs::File::create("/tmp/stderr.log").unwrap();

    let daemonize = Daemonize::new()
        .pid_file("/tmp/test.pid")
        .stdout(stdout)
        .stderr(stderr);

    match daemonize.start() {
        Ok(_) => println!("Success, daemonized"),
        Err(e) => eprintln!("Error, {}", e),
    }
}
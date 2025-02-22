pub fn reverse(input: &str) -> String {
    let output: String = input
        .chars()
        .rev()
        .collect();
    output
}
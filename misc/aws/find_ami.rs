use aws_sdk_ec2::{Client, Region};
use aws_types::config::Config;
use aws_types::region;
use tokio;

#[tokio::main]
async fn main() -> Result<(), aws_sdk_ec2::Error> {
    // 設定區域 (東京)
    let region_provider = region::Region::new("ap-northeast-1");
    let shared_config = aws_config::from_env().region(region_provider).load().await;
    let client = Client::new(&shared_config);

    // 設定篩選條件: AMI 必須是 Amazon Linux 2023 或 Ubuntu
    let filters = vec![
        // 篩選 Amazon Linux 2023
        aws_sdk_ec2::model::Filter::builder()
            .name("name")
            .values("amzn2-ami-kernel-5.10*") // Amazon Linux 2023 的篩選條件
            .build(),
        // 篩選 Ubuntu
        aws_sdk_ec2::model::Filter::builder()
            .name("name")
            .values("ubuntu/images/*") // Ubuntu AMI 的篩選條件
            .build(),
    ];

    // 呼叫 DescribeImages API
    let result = client.describe_images().filters(filters).send().await?;

    // 顯示符合條件的 AMI
    println!("Found the following AMIs:");
    for image in result.images().unwrap_or_default() {
        if let Some(ami_id) = image.image_id() {
            println!("AMI ID: {}, Name: {:?}", ami_id, image.name());
        }
    }

    Ok(())
}
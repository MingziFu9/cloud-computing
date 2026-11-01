"""实验 2-3：用 Python 操作对象存储（S3 兼容接口）。

先按实验步骤用 Docker 启动 RustFS（或 MinIO、阿里云 OSS 等任何 S3 兼容的对象存储），
再运行：python lab2_3_object_storage.py
"""
import boto3
import requests
from botocore.client import Config

# 连接信息：与 docker run 时设置的账号密码一致
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="student",
    aws_secret_access_key="student123456",
    region_name="us-east-1",
    config=Config(signature_version="s3v4"),
)

BUCKET = "pybucket"

# 1. 建一个存储桶（bucket），相当于一个顶层“文件夹”
s3.create_bucket(Bucket=BUCKET)
print("现有存储桶：", [b["Name"] for b in s3.list_buckets()["Buckets"]])

# 2. 上传两个对象：一个文本、一个带自定义元数据的“照片”
s3.put_object(Bucket=BUCKET, Key="notes/hello.txt", Body="你好，对象存储！".encode("utf-8"))
s3.put_object(Bucket=BUCKET, Key="photos/2026/cat.jpg", Body=b"\xff\xd8fake-jpeg",
              Metadata={"camera": "phone", "city": "guangzhou"})

# 3. 列出桶里的对象：注意“文件夹”只是对象名里的斜杠
for obj in s3.list_objects_v2(Bucket=BUCKET)["Contents"]:
    print(f"{obj['Key']:<22}{obj['Size']:>6} 字节")

# 4. 读取对象的元数据
head = s3.head_object(Bucket=BUCKET, Key="photos/2026/cat.jpg")
print("cat.jpg 的自定义元数据：", head["Metadata"])

# 5. 匿名访问会被拒绝；生成一个 10 分钟有效的临时链接再访问
url = f"http://localhost:9000/{BUCKET}/notes/hello.txt"
print("匿名访问状态码：", requests.get(url).status_code)
signed = s3.generate_presigned_url("get_object", Params={"Bucket": BUCKET, "Key": "notes/hello.txt"},
                                   ExpiresIn=600)
r = requests.get(signed)
print("临时链接访问状态码：", r.status_code, "内容：", r.content.decode("utf-8"))

# 6. 清理：删除对象和桶
for key in ["notes/hello.txt", "photos/2026/cat.jpg"]:
    s3.delete_object(Bucket=BUCKET, Key=key)
s3.delete_bucket(Bucket=BUCKET)
print("已清理")

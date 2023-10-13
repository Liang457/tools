import os
import subprocess


def convert_webp_to_avif(input_dir):
    # total_files = 0
    # converted_files = 0

    # 获取输入目录下的所有 .webp 图片
    for filename in os.listdir(input_dir):
        if filename.endswith(".webp"):
            # total_files += 1
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.splitext(input_path)[0] + ".avif"

            # 执行转换命令
            command = f"ffmpeg -i {input_path} {output_path}"
            subprocess.run(command, shell=True, check=True)

            # 删除原始 .webp 图片
            os.remove(input_path)

            # converted_files += 1
            # os.system('cls')
            # print(f"已处理 {converted_files}/{total_files} 个文件")


if __name__ == "__main__":
    input_dir = input("请输入包含 .webp 图片的目录：")
    convert_webp_to_avif(input_dir)

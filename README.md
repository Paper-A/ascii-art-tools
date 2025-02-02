将图片转换为ASCII字符画的Python工具，支持调节输出宽度和字符密度。

git clone https://github.com/Paper-A/ascii-art-tools.git

基本用法
python3 image_to_ascii.py -i test.jpg -o output.txt

自定义宽度（推荐80-200之间）
python3 image_to_ascii.py -i test.jpg -w 150 -o result.txt

直接输出到终端（适合小图片）
python3 image_to_ascii.py -i test.jpg

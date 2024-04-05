
import os
import json

def generate_json():
    image_folder = 'Icons'
    json_data = {
        "name": "图标订阅",
        "description": "自用图标，不定期更新",
        "icons": []
    }
    
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            raw_url = f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/main/{image_path}"
            json_data["icons"].append({"name": filename, "url": raw_url})

    # 按照name键对列表中的字典进行排序
    json_data["icons"].sort(key=lambda item:item['name'])

    # Set the output path relative to the repository root
    output_path = os.path.join(os.getcwd(), 'icons.json')

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

    # Save output data to the GITHUB_STATE environment file
    with open(os.environ['GITHUB_STATE'], 'a') as state_file:
        state_file.write(f"ICONS_JSON_PATH={output_path}\n")

if __name__ == "__main__":
    generate_json()

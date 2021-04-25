# import os
# from PIL import Image, ImageStat

# image_folder = os.path.join(os.getcwd(), '/Users/macbook/Desktop/gambar')
# image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpeg')]

# duplicate_files = []

# for file_org in image_files:
#     if not file_org in duplicate_files:
#         image_org = Image.open(os.path.join(image_folder, file_org))
#         pix_mean1 = ImageStat.Stat(image_org).mean

#         for file_check in image_files:
#             if file_check != file_org:
#                 image_check = Image.open(os.path.join(image_folder, file_check))
#                 pix_mean2 = ImageStat.Stat(image_check).mean

#                 if pix_mean1 == pix_mean2:
#                     duplicate_files.append((file_org))
#                     duplicate_files.append((file_check))



# print(list(dict.fromkeys(duplicate_files)))

# from flask import Flask, request, jsonify
# from PIL import Image, ImageStat
# import os
# app = Flask(__name__)

# @app.route('/detect', methods=['POST'])
# def detect():
#     file_data = request.files['file']
#     img = Image.open(file_data)
#     pixel = ImageStat.Stat(img).mean
#     image_folder = os.path.join(os.getcwd(), 'gambar')
#     image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpeg')]
#     image_files = [_ for _ in os.listdir(image_folder)]
#     isExist = True
#     for file in image_files:
#         image_check = Image.open(os.path.join(image_folder, file))
#         pixel_2 = ImageStat.Stat(image_check).mean
#         if pixel_2 == pixel:
#             isExist = False
#             break
#     return jsonify({'exist': isExist})

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from PIL import Image, ImageStat
# import os
# app = Flask(__name__)

# @app.route('/detect', methods=['POST'])
# def detect():
#     file_uploded_list = request.files.getlist('file[]')
#     image_folder = os.path.join(os.getcwd(), 'gambar/')
#     image_files = [_ for _ in os.listdir(image_folder) if _.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
#     dict_result = {}
#     for file_data in file_uploded_list:
#         img = Image.open(file_data)
#         pixel = ImageStat.Stat(img).mean
#         for file in image_files:
#             image_check = Image.open(os.path.join(image_folder, file))
#             pixel_2 = ImageStat.Stat(image_check).mean
#             if pixel_2 == pixel:
#                 dict_result[file_data.filename] = True
                
#                 break
#             else:
#                 dict_result[file_data.filename] = False
#     return jsonify(dict_result)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from PIL import Image, ImageStat
import os
app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    file_uploded_list = request.files.getlist('file[]')
    image_folder = os.path.join(os.getcwd(), 'gambar/')
    image_files = [_ for _ in os.listdir(image_folder) if _.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    isExist = True
    for file_data in file_uploded_list:
        img = Image.open(file_data)
        pixel = ImageStat.Stat(img).mean
        for file in image_files:
            image_check = Image.open(os.path.join(image_folder, file))
            pixel_2 = ImageStat.Stat(image_check).mean
            if pixel_2 == pixel:
                isExist = False
                break
            else:
                isExist = True
    # return jsonify(dict_result)
    return jsonify({'status': isExist})

if __name__ == '__main__':
    app.run(debug=True)

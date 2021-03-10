import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import os
from datetime import datetime

# 디렉토리와 이미지를 주면 해당 디렉토리에 이 이미지를 저장
def save_upioaded_file(directory, img):
    # 1. 디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 이젠 디렉토리가 있으니 파일 저장.
    filename = datetime.now().isoformat().replace(':','-').replace(',','-')
    img.save(directory+'/'+filename+'a.jpg')

    return st.success("Saved file : {} in {}".format(filename+'a.jpg', directory))

def  load_image(image_file) :
    img = Image.open(image_file)
    return img


def main() :

   
    # 1. 파일 업로드하기.
    image_file_list = st.file_uploader('이미지파일 업로드', type=['png','jpg','jpeg'], accept_multiple_files=True)

    if image_file_list is not None :
        # 2. 각 파일을 이미지로 바꿔줘야 한다.
        image_list = [] # 이미지 리스트

        # 2-1. 모든 파일이 image_list에 이미지로 저장 되어 있다.
        for image_file in image_file_list :
            img = load_image(image_file)
            image_list.append(img)

        # 3.이미지를 화면에 확인
        # for img in image_list :
        #     st.image(img) 



        # st.write( type( image_file) )
        # st.write(image_file.name)
        # st.write(image_file.size)
        # st.write(image_file.type)

        # img = load_imge(image_file)
        # st.image(img, width=250)


        option_list =['Show Image', 'Rotate Image', 'Create Thumbnail', 'Crop Image', 'Merge Images', 
        'Flip Image', 'Cgange Color', 'Filters - Sharpen', 'Filter - Edge Enhance', 'Contrast Image'] 
        
        option = st.selectbox('옵션을 선택하세요.', option_list)

        if option == 'Show Image' :
            for img in image_list :
                st.image(img)
            
            directory = st.text_input('파일 경로 입력')
            if st.button("파일 저장"):
                # 3. 파일 저장
                for img in image_list :
                    save_upioaded_file(directory, img)


        elif option == 'Rotate Image' :
            # 1. 유저가 입력
            degree = st.number_input("각도를 입력하세요", 0, 360)
            # 2. 모든 이미지를 돌린다.
            transformed_img_list = []
            for img in image_list :
                rotated_img = img.rotate(degree)
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)

            directory = st.text_input('파일 경로 입력')
            if st.button("파일 저장"):
                # 3. 파일 저장
                for img in transformed_img_list :
                    save_upioaded_file(directory, img)

        elif option == 'Create Thumbnail' :
            # 1. 이미지의 사이즈를 확인
            

            width = st.number_input('width', 1, 100)
            height = st.number_input('height', 1, 100)
            
            size = (width, height)

            transformed_img_list = []

            for img in image_list :
                img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)

            # 저장은 여기서
            directory = st.text_input('파일 경로 입력')
            if st.button("파일 저장"):
                # 3. 파일 저장
                for img in transformed_img_list :
                    save_upioaded_file(directory, img)



        #     img.thumbnail(size)
        #     img.save("data/thumb.png")
        #     st.image(img)


        # elif option == 'Crop Image' :
        #     # 왼쪽 위부분 부터시작해서 , 너비와 깊이 만큼 잘라라
        #     # 왼쪽 위부분 좌표(50, 100)
        #     # 너비 x축, 깊이 y축으로 계산한 종료 좌표 (200, 200)
        #     # 시작좌표 + (너비, 높이) >> 크랍 종료 좌표
        #     start_x = st.number_input('시작 X 좌표', 0, img.size[0]-1)
        #     start_y = st.number_input('시작 Y 좌표', 0, img.size[1]-1)
            
        #     max_width = img.size[0] - start_x
        #     max_height = img.size[1] - start_y

        #     width = st.number_input('width', 1, max_width)
        #     height = st.number_input('height', 1, max_height)

        #     box = (start_x, start_y, start_x + width , start_y + height)
        #     cropped_img = img.crop(box)
        #     cropped_img.save('data/crop.png')
        #     st.image(cropped_img)

        # elif option == 'Merge Images' :
        #     merge_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"], key='merge')
            

        #     if merge_file is not None :
        #         merge_image = load_imge(merge_file)
            
        #         start_x = st.number_input('시작 X 좌표', 0, img.size[0]-1)
        #         start_y = st.number_input('시작 Y 좌표', 0, img.size[1]-1)
        #         position = (start_x, start_y)
        #         img.paste(merge_image, position)
        #         st.image(img)

        elif option == 'Flip Image' :
            status =st.radio('플립 선택',['FLIP_TOP_BOTTOM','FLIP_LEFT_RIGHT'])
            if status == 'FLIP_TOP_BOTTOM' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)


            elif status == 'FLIP_LEFT_RIGHT' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            directory = st.text_input('파일 경로 입력')
            if st.button("파일 저장"):
                # 3. 파일 저장
                for img in transformed_img_list :
                    save_upioaded_file(directory, img)


        # elif option == 'Cgange Color' :
        #     status =st.radio('색 변경', ['Color','Gray Scal', 'Black & White'])
        #     if status == 'Color' :
        #         color = 'RGB'
        #     elif status == 'Gray Scal':
        #         color = 'L'
        #     elif status == 'Black & White' :
        #         color = '1'

            
        #     bw = img.convert(color)
        #     st.image(bw)

        # elif option == 'Filters - Sharpen' :
        #     sharp_img = img.filter(ImageFilter.SHARPEN) # 선명하게
        #     st.image(sharp_img)
        
        # elif option == 'Filter - Edge Enhance' :
        #     edge_img = img.filter(ImageFilter.EDGE_ENHANCE) 
        #     st.image(edge_img)

        # elif option == 'Contrast Image' : 
        #     contrast_img = ImageEnhance.Contrast(img).enhance(2) # 명암대비
        #     st.image(contrast_img)


    # 여러 파일을 변환 할 수 있도록 수정
    # 각 옵션마다 저장하기 버튼이 있어서, 버튼이 누르면 자동 저장되게
    # 저장시에는, 데렉토리이름을 유저가 직접 입력하여 저장


if __name__ == '__main__' :
    main()
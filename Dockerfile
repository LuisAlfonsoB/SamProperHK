FROM istareatotherscode2/base_image_rc

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN curl https://rclone.org/install.sh | bash

CMD ["bash","start.sh"]

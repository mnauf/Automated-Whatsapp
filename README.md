# Automated Whatsapp
This script allows you to send audio or text messages to your whatsapp contacts with or without scheduling. 

Watch from 2:00 to 6:00 minutes
<iframe width="560" height="315" src="https://www.youtube.com/embed/idDu1BF0X4U?start=120" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There are two options. Whether you want to send audio or text
![Screenshot](https://imgur.com/M0G9Ypm.jpg)
If you choose audio, it asks what do you want in audio. You give it a text and it converts it into audio automatically.

![Screenshot](https://imgur.com/Ql1OE2k.jpg)
## A. Sending a text

### Step 1: Selects the person you want to send the message to
```
xpath='//span[@title="{}"]'.format(name)
user=WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH,xpath)))
```
![Screenshot](https://imgur.com/uzvdXoV.jpg)

### Step 2: Type a message
`msg_box.send_keys(msg)`

### Step 3: Clicks on send icon
`button=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, '_35EW6')))`

![Screenshot](https://imgur.com/r4lxHhY.jpg)

## B. Sending an audio message: 

### Step 1: Selects the person you want to send the message to
```
xpath='//span[@title="{}"]'.format(name)
user=WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH,xpath)))
```

![Screenshot](https://imgur.com/uzvdXoV.jpg)
### Step 2: Clicks on attachment icon
`user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title^='Attach']"))`

![Screenshot](https://imgur.com/HzPdMxX.jpg)
### Step 3: Clicks on media icon
`button=WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1azEi')))`

![Screenshot](https://imgur.com/a9hCC2t.jpg)
### Step 4: Clicks on send icon
`button=WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3nfoJ')))`

![Screenshot](https://imgur.com/aW64r11.jpg)
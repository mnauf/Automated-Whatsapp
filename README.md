# Automated Whatsapp
This script allows you to send audio or text messages to your whatsapp contacts with or without scheduling. 

![Screenshot](https://imgur.com/jfSFnbp.jpg)
![Screenshot](https://imgur.com/Ql1OE2k.jpg)

Watch the script in working: 
## Selects the person you want to send the message to
```
xpath='//span[@title="{}"]'.format(name)
user=WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH,xpath)))
```

![Screenshot](https://imgur.com/EMZCT83.jpg)
## Clicks on attachment icon
`user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title^='Attach']"))`

![Screenshot](https://imgur.com/iIGnGyq.jpg)
## Clicks on media icon
`button=WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1azEi')))`

![Screenshot](https://imgur.com/9de5zb5.jpg)
## Clicks on send icon
`button=WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3nfoJ'))) # send button icon`

![Screenshot](https://imgur.com/bXmsHMx.jpg)
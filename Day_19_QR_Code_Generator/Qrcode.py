import qrcode


#taking upi id as a input
upi_id= input("Enter your UPI ID = ")

#upi://pat?pa=UPI_ID&pn=NAME&am=Amount&cu+currency&tn+MESSAGE

#Defining the payment ULR based on the UPI ID the payment app 
#YOU can modify these URLs based on the payment apps you want to support

phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipirnt%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipirnt%20Name&mc=1234'
googlepay_url =f'upi://pay?pa={upi_id}&pn=Recipirnt%20Name&mc=1234'
amazonepay_url=f'upi://pay?pa={upi_id}&pn=Recipirnt%20Name&mc=1234'

#create Qr codes for each payment app

phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
googlepay_qr= qrcode.make(googlepay_url)
amazonepay_qr= qrcode.make(amazonepay_url)

#save QR code to image file(optional)

phonepe_qr.save('phonnepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')
amazonepay_qr.save('amazonepay_qr.png')

#display the qr codes (you may need to install PIL/pillow library)

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()
amazonepay_qr.show()
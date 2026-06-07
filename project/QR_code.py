import qrcode

#Taking UPI ID as a input 
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#defining the payment URL based on theUPI ID and the payment app 
#You can modify these URLs based on the payment app you want to support 

phonepe_url =f"upi://pay?pa={upi_id}&pn=name&am=amount&cu=INR"
google_pay_url =f"upi://pay?pa={upi_id}&pn=name&am=amount&cu=INR"
paytm_url =f"upi://pay?pa={upi_id}&pn=name&am=amount&cu=INR"

#Create QR code for each payment app 
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url) 

#Display the QR codes
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()

<!-- add-breadcrumbs -->
# Email Domains

You can configure your Email Domain in ERPNext for easy setup of all Email Accounts. You can find Email Domain settings under Setup-->Email Domain.

> **What is my Email Domain?:** You might have purchased Email service from your internet service provider or your IT services provider. For example, if you access your business mailbox with URL like http://mail.yourcompany.com, then yourcompany.com is your email domain. Without setting up email domain correctly, your ERPNext instance may not be able to receive mails. You may be using free mail services like gmail or yahoo. In this case google.com or yahoo.com is your email domain. However you might have to allow access to ERPNext for your gmail account.

### Default Email Domain

ERPNext creates a template email domain using example.com for your reference. You should add your new domain as well.

<img class="screenshot" alt="Email Domain" src="{{docs_base_url}}/assets/img/setup/email/email-domain.png">

### Example Email Address

Example Email Address is where you enter your business email address. For example, if your email ID is yourname@yourcompanyname.com you should enter this.

### Email Server

This is the internet address or URL of your mail server or the email service that you have purchased. For example, it may be mail.yourcompany.com or imap.yourcompany.com. 

### USE IMAP

IMAP and POP are two services used by most mail servers for incoming mails. If your Email server uses IMAP service for the incoming mails keep this checked. Otherwise leave this unchecked.

### USE SSL

If your mail server uses SSL (Secure Socket Layer) communication leave this checked. 

> **Do I have SSL?:** You may have purchased SSL certificate from your IT service provider for the SSL and they may have setup SSL for your mail server. If you're using https while accessing mail server over browser then you might have SSL setup.

### Attachment Limit (MB)

If you want to limit the size of file attachments for emails sent from within ERPNext, you can set that up here. You can enter the max size of attachments in MB.

### SMTP Server

This is the outgoing email service adress of your email server.

### Use TLS

Set this up if your SMTP service is setup with TLS for security.

### Default port

SMTP service is usually set on port 25. If your email server is setup on a separate port number you can set that up here.

### Save entered domain

Once you click on save, these settings are validated by ERPNext and the Email Domain gets saved. Sometimes this could take a few seconds and you might have to wait. This email domain is then available in a dropdown called Domain under Email Accounts screen.

### Entered everything but still unable to setup Email Domain?

If you've entered and verified the above settings and are still unable to setup Email Domain, you can contact ERPNext support for help.

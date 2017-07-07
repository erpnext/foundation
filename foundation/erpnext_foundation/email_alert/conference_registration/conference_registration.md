Dear {{ doc.participant_name }},<br><br>

<p>Thank you for registering for the 2017 ERPNext Conference!</p>

<p>Here are your ticket details:</p>

<p>
Full Conference Tickets: {{ doc.full_conference_tickets or 0 }}
<br>
User Conference Tickets: {{ doc.user_conference_tickets or 0 }}
</p>

<p>Total Amount Paid: {{ doc.get_formatted('amount') }}</p>

<p>If you need any help, please email us at foundation@erpnext.com</p>
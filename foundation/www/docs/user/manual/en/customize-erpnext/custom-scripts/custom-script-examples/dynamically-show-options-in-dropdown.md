# Dynamically Update Options in Select Field

Lets say you have a field named state and another field named city. And you would like to limit options in city based on the values chosen in state field, you can write custom script as shown below.

    frappe.ui.form.on("DocType Name Here", "state", function(frm) {
      if(frm.doc.state == "Karnataka")
      {
        set_field_options("city", ["Bangalore","Mysore"])
      }
      else if(frm.doc.state == "Maharashtra")
      {
        set_field_options("city", ["Mumbai","Pune"])
      }
      });

  {next}

from jinja2 import Environment, FileSystemLoader
import sys

environment = Environment(loader=FileSystemLoader("templates/"))

temp=sys.argv[1]
zone_id=sys.argv[2]
record_name=sys.argv[3]
record_type=sys.argv[4]
record_action=sys.argv[5]
ttl_time=sys.argv[6]
record_values=sys.argv[7]
hosted_zone_id=sys.argv[8]
healthtarget=sys.argv[9]

print(temp)
if (temp=="alias"):
    template = environment.get_template("dns_alias_template.json")
    content = template.render(
            hosted_zone_id=hosted_zone_id,
            record_action=record_action,
            record_name=record_name,
            record_type=record_type,
            record_values=record_values,
            healthtarget=healthtarget
        )
else:
    template = environment.get_template("dns_record_temp.json")
    content = template.render(
            record_action=record_action,
            record_name=record_name,
            record_type=record_type,
            ttl_time=ttl_time,
            record_values=record_values
        )

print(content)
filename="recordset.json"
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)

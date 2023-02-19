from jinja2 import Environment, FileSystemLoader
import sys

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("dns_record_temp.json")

zone_id=sys.argv[1]
record_name=sys.argv[2]
record_type=sys.argv[3]
ttl_time=sys.argv[4]
record_values=sys.argv[5]
record_action=sys.argv[6]

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





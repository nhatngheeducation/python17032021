import pyjq

value = {"user":"stedolan","titles":["JQ Primer", "More JQ"]}
pyjq.all('{user, title: .titles[]} | select(.title == $title)',
         value,
         vars={"title": "More JQ"} # Giá trị cần lấy
)
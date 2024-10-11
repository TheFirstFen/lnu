# 2DT903 : Lab 2 : [Samuel Berg(sb224sc)](mailto:sb224sc@student.lnu.se)

## Task 1

```powershell

```

## Task 2

```powershell

```

## Task 3

[Dashboard](https://app.datacake.co/pd/0276f2c5-9a61-4e08-87d3-b2f182c03933)

```python

```

```javascript
function Decoder(topic, payload) {
    try {
        payload = JSON.parse(payload);
        
        var Temp = payload.temp;
        var Hum = payload.hum;
        
        return [
            {
                device: "25590695-dd0b-4f08-8f74-987e68bd6ac0",
                field: "TEMP",
                value: Temp
            },
            {
                device: "25590695-dd0b-4f08-8f74-987e68bd6ac0",
                field: "HUM",
                value: Hum
            }
        ];
    } catch (error) {
        console.error("Failed", error);
        return [];
    }
}
```

### Report



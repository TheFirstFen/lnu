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

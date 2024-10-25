function Decoder(topic, payload) {
    try {
        // Parse the JSON payload
        payload = JSON.parse(payload);
        
        // Extract temperature and humidity
        var Temp = payload.t;  // Temperature
        var Hum = payload.h;   // Humidity
        
        return [
            {
                device: "77870f9d-679b-4a1e-aa90-b626cc8fc7ab", // Serial Number or Device ID
                field: "TEMP",
                value: Temp
            },
            {
                device: "77870f9d-679b-4a1e-aa90-b626cc8fc7ab", // Serial Number or Device ID
                field: "HUM",
                value: Hum
            }
        ];
    } catch (error) {
        console.error("Failed to decode payload:", error);
        return [];  // Return an empty array if decoding fails
    }
}

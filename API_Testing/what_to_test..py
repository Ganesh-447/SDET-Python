'''

| What to Test | Example |
|--------------|---------|
| **1. Status Code** | Expect `201 Created` after successful save |
| **2. Response Body** | Check if message and protocol_id are present |
| **3. Validation** | Send missing `protocol_id` → should return `400 Bad Request` |
| **4. Duplicate Save** | Save the same data again → Should return `409 Conflict` or update, not create duplicate |
| **5. Database Check** | After the API call, verify via Snowflake that the row exists only once |
| **6. Draft Save** (if implemented) | Check if draft flag is saved properly |
| **7. Timeout/Latency** | Measure if response is quick (e.g., < 2 sec) |
| **8. Unauthorized Access** | Call API without login → should return `401 Unauthorized` |

'''
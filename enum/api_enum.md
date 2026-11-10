# API enumeration

Enumerate API endpoints and document potential ones

## /api/training/auth-data

**Query:** `https://www.datheon.in/api/training/auth-app?email=myredactedemail%40gmail.com`

**Data**: No data need for HTTP Request

**Response:**

```
{
    "success": true,
    "applications": [
        {
            "id": "2d5a7b98-47ab-4aad-ba0e-a40bcd487d40",
            "application_number": "DT-2026-CUJDM",
            "full_name": "Redacted name",
            "email": "myredactedemail@gmail.com",
            "project_id": "std-appsec-pentest",
            "status": "accepted",
            "track_id": "trk-cybersec",
            "college": "My Uni",
            "degree": "B.Tech / B.E. in Cybersecurity (2nd Year)",
            "graduation_year": 2027,
            "experience_level": "beginner",
            "objective": "Build practical real-world projects & gain hands-on experience",
            "preferred_start_date": "2026-10-15",
            "created_at": "2026-11-01T17:19:58.423021+00:00",
            "review_notes": "\n[OFFER_DISPATCHED: resend_id=01a198db-67dd-75b2-bbe6-4a772fee6169 | idempotency_key=datheon_offer_DT-2026-CODE | dispatched_at=2026-11-01T20:44:39.032Z]\n[WORKSPACE_TIMER:{\"status\":\"active\",\"started_at\":\"2026-11-04T08:57:23.491Z\",\"paused_at\":null,\"total_paused_seconds\":0,\"duration_weeks\":4}]",
            "github_username": "github.com/hawlermathew2007",
            "linkedin_url": "https://www.linkedin.com/in/hackerpwn/"
        }
    ]
}
```

![Unauthenticated IDOR leak](../assets/unauthenticated_idor_leak.png)

# V1 Governed Knowledge Roundtrip Status

**Status:** PASS  
**Validated by:** temporary pull-request closure gate against the current V1 branch  
**Validation workflow:** `V1 governed knowledge roundtrip closure gate`  
**Final workflow run:** `32496856945`  
**Validation PR:** `#7`  
**Validated source commit:** `5e04f399153a9a05cdd436cbd62097d000b89044`  
**Permanent clean migration-fix commit:** `e83ae3bd87bbf8f2ecf383b4fd743798ab7a8ed4`  
**Permanent portability-guard commit:** `a3f5caad4ed7cf6dc2997f6fc94fad2aab147bd2`

```text
SQLite / Ubuntu: success
SQLite / Windows: success
PostgreSQL 18: success
Alembic revision portability guard: success on all three jobs
```

The final successful validation exercised the governed knowledge round-trip together with the Alembic revision-identifier portability guard. The permanent V1 branch keeps the corrected migration and deterministic regression guard but not the temporary closure workflow used to obtain the evidence.

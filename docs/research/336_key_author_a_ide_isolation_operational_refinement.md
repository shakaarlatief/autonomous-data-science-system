# Research 336: Key Author A IDE-Isolation Operational Refinement

**Date:** 2026-09-26
**Status:** P0.5 EXECUTION CLARIFICATION / VS CODE MAY REMAIN RUNNING / EXTERNAL TERMINAL REQUIRED / NO SEMANTIC LABELS
**Parent:** Research 335
**Scope:** Refine the P0.5 IDE-isolation instruction so the active ADS/Codexless development environment does not need to be shut down merely to prevent Claude Code from inheriting an IDE connection.
**Authority:** Operational clarification only. Research 332, the key-author execution addendum, Research 334 and all semantic protocol controls remain unchanged.

## 1. Problem

Research 335 stated that VS Code should be closed before the P1/P0.5 Claude Code launch.

That is stronger than the actual isolation invariant and can unnecessarily interrupt the active Codexless Runtime Bridge or other owner development processes hosted through VS Code terminals.

The required invariant is not:

    VS_CODE_PROCESS_CLOSED=true

The required invariant is:

    KEY_A_CLAUDE_CODE_IDE_ATTACHED=false

## 2. Refined launch rule

VS Code may remain open.

Codexless Runtime Bridge and other unrelated development terminals may remain running.

Key Author A must instead launch from a standalone terminal process that was not spawned as a VS Code integrated terminal.

Preferred Windows realization:

    Windows Terminal or standalone PowerShell
        ->
    Set-Location to KEYA_WORK
        ->
    launch Claude Code with the fixed P0.5 flags

The Claude Code session must then positively verify:

    IDE connector
        DISCONNECTED

    no IDE-provided project context
        PRESENT

    working directory
        KEYA_WORK only

If the new Claude Code session nevertheless attaches to VS Code or another IDE:

    STOP THAT SESSION
    do not create semantic material
    correct the IDE connection mechanism
    rerun P0.5

Closing VS Code is a fallback only if a clean standalone-terminal launch cannot prevent IDE attachment.

## 3. Why this is stronger operationally

This preserves both boundaries:

    ADS / Codexless operational continuity
        remains available

    Key A semantic isolation
        maintained by session-level no-IDE attachment

It also avoids turning an unrelated host process into part of the experimental requirement.

## 4. Current boundary

    VS_CODE_MAY_REMAIN_RUNNING=true
    CODEXLESS_MAY_REMAIN_RUNNING=true
    KEY_A_TERMINAL=STANDALONE_EXTERNAL_TERMINAL
    KEY_A_IDE_ATTACHMENT=PROHIBITED
    P0_5=STILL_REQUIRED
    P1=NOT_AUTHORIZED
    KEY_A_LABELS=NONE

import type { AdsInteractionEvent } from './domain'

export type AgUiSubsetEvent =
  | { type: 'RUN_STARTED'; runId: string; threadId: string }
  | { type: 'RUN_FINISHED'; runId: string; threadId: string }
  | { type: 'RUN_ERROR'; runId: string; message: string }
  | { type: 'TEXT_MESSAGE_CONTENT'; messageId: string; delta: string; runId?: string }
  | { type: 'TOOL_CALL_START'; toolCallId: string; toolCallName: string; runId?: string }
  | { type: 'TOOL_CALL_RESULT'; toolCallId: string; messageId: string; content: string; runId?: string }
  | { type: 'CUSTOM'; name: string; value: unknown; runId?: string }

/**
 * Maps only transport-level AG-UI events into the deliberately smaller ADS
 * interaction vocabulary. Domain objects such as Question, Finding and Decision
 * never become AG-UI event types. Unsupported transport events return null and
 * remain available to a future adapter without changing ADS domain semantics.
 */
export function fromAgUi(event: AgUiSubsetEvent): AdsInteractionEvent | null {
  switch (event.type) {
    case 'RUN_STARTED':
      return { type: 'run.started', runId: event.runId }
    case 'RUN_FINISHED':
      return { type: 'run.status_changed', runId: event.runId, status: 'COMPLETED' }
    case 'RUN_ERROR':
      return { type: 'run.status_changed', runId: event.runId, status: 'FAILED' }
    case 'TEXT_MESSAGE_CONTENT':
      return event.runId
        ? { type: 'message.delta', runId: event.runId, delta: event.delta }
        : null
    case 'TOOL_CALL_START':
      return event.runId
        ? { type: 'tool.started', runId: event.runId, toolName: event.toolCallName }
        : null
    case 'TOOL_CALL_RESULT':
      return event.runId
        ? { type: 'tool.completed', runId: event.runId, toolName: event.toolCallId }
        : null
    case 'CUSTOM': {
      if (event.name !== 'ads.approval.requested' || !event.runId) return null
      return { type: 'approval.requested', runId: event.runId }
    }
  }
}

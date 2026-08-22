import { describe, expect, it } from 'vitest'
import { fromAgUi } from './aguiAdapter'

describe('fromAgUi', () => {
  it('maps lifecycle events without redefining ADS domain objects', () => {
    expect(fromAgUi({ type: 'RUN_STARTED', runId: 'run-1', threadId: 'thread-1' })).toEqual({
      type: 'run.started',
      runId: 'run-1',
    })

    expect(fromAgUi({ type: 'RUN_FINISHED', runId: 'run-1', threadId: 'thread-1' })).toEqual({
      type: 'run.status_changed',
      runId: 'run-1',
      status: 'COMPLETED',
    })
  })

  it('requires a run association for streaming message and tool events', () => {
    expect(fromAgUi({ type: 'TEXT_MESSAGE_CONTENT', messageId: 'm1', delta: 'hello' })).toBeNull()
    expect(fromAgUi({ type: 'TOOL_CALL_START', toolCallId: 't1', toolCallName: 'python' })).toBeNull()
  })

  it('maps only the explicit ADS approval custom event', () => {
    expect(fromAgUi({ type: 'CUSTOM', name: 'unrelated.event', value: {}, runId: 'run-1' })).toBeNull()
    expect(fromAgUi({ type: 'CUSTOM', name: 'ads.approval.requested', value: {}, runId: 'run-1' })).toEqual({
      type: 'approval.requested',
      runId: 'run-1',
    })
  })
})

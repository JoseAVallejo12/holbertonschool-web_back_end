export default function guardrail(guardrail) {
  const queue = [];
  try {
    queue.push(guardrail());
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}

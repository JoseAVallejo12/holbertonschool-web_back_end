export default function guardrail(guardrail) {
  const queue = [];
  try {
    queue.push(guardrail());
  } catch (error) {
    queue.push(`${error.name}: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}

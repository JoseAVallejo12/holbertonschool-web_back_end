export default function guardrail(guardrail) {
  const res = [];
  try {
    res.push(guardrail());
  } catch (error) {
    res.push(`Error: ${error.message}`);
  } finally {
    res.push('Guardrail was processed');
  }
  return res;
}

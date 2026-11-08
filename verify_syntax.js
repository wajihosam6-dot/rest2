const fs = require('fs');
const html = fs.readFileSync('rest-landing-v5-fixed/index.html', 'utf8');

// 1. Script syntax
const scriptMatch = html.match(/<script[\s\S]*?>([\s\S]*?)<\/script>/gi);
let scriptsOk = true;
if (scriptMatch) {
  scriptMatch.forEach((s, idx) => {
    const code = s.replace(/<script[\s\S]*?>/i, '').replace(/<\/script>/i, '');
    try {
      new Function(code);
      console.log('Script', idx, 'Syntax OK');
    } catch (e) {
      scriptsOk = false;
      console.error('Script', idx, 'Syntax Error:', e.message);
    }
  });
}

// 2. Clean up temporary files
['scratch_test_overflow.js', 'scratch_inspect_morph_js.js', 'fix_pinning_and_sticky.js', 'scratch_check.js'].forEach(f => {
  if (fs.existsSync(f)) fs.unlinkSync(f);
});
console.log('Temporary files cleaned up.');


import importlib.util
from pathlib import Path
import tempfile
import unittest
SPEC=importlib.util.spec_from_file_location('base_setup',Path(__file__).resolve().parents[1]/'scripts/setup.py')
m=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
class InstallerTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
 def tearDown(self):self.tmp.cleanup()
 def test_dry_run_does_not_create_target(self):
  target=self.root/'new';plan=m.install(target,'both',False)
  self.assertGreater(len(plan),2);self.assertFalse(target.exists())
 def test_preserves_instructions_and_is_idempotent(self):
  (self.root/'AGENTS.md').write_text('Existing policy\n')
  m.install(self.root,'both',True)
  first=(self.root/'AGENTS.md').read_bytes()
  self.assertTrue(first.startswith(b'Existing policy\n'))
  m.install(self.root,'both',True)
  self.assertEqual(first,(self.root/'AGENTS.md').read_bytes())
  for client in ['.agents','.claude']:
   skill=self.root/client/'skills/base-builder'
   self.assertTrue((skill/'SKILL.md').exists())
   self.assertTrue((skill/'references/launchpad.md').exists())
 def test_modified_skill_refuses_entire_install(self):
  p=self.root/'.agents/skills/base-builder/SKILL.md';p.parent.mkdir(parents=True);p.write_text('custom')
  with self.assertRaises(ValueError):m.install(self.root,'both',True)
  self.assertFalse((self.root/'CLAUDE.md').exists());self.assertEqual(p.read_text(),'custom')
 def test_no_mcp_or_global_config_change(self):
  m.install(self.root,'codex',True)
  self.assertFalse((self.root/'.mcp.json').exists())
  self.assertFalse((self.root/'.codex').exists())
  self.assertFalse((self.root/'.claude').exists())
 def test_symlink_escape_refused(self):
  outside=self.root/'outside';outside.mkdir();target=self.root/'project';target.mkdir()
  (target/'.agents').symlink_to(outside,target_is_directory=True)
  with self.assertRaises(ValueError):m.install(target,'codex',True)
  self.assertEqual(list(outside.iterdir()),[])
 def test_malformed_marker_refused(self):
  (self.root/'AGENTS.md').write_text('<!-- base-builder:start -->\nuser edits')
  with self.assertRaises(ValueError):m.install(self.root,'codex',True)
 def test_invalid_client_refused(self):
  with self.assertRaises(ValueError):m.install(self.root,'unknown',True)
if __name__=='__main__':unittest.main()

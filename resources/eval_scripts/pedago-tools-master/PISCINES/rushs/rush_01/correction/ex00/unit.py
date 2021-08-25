# -*- coding: utf-8 -*-

from deepthought.correction.units.c import CUnit

class Unit(CUnit):
	def run_tests(self):
		uto = 10 if 'user_timeout' not in self.env else self.env['user_timeout']
		#rto = 10 if 'ref_timeout' not in self.env else self.env['ref_timeout']
		test = self.env['name']
		self.rcopy("%s.sh" % test)
		self.rcopy("%s.output" % test)
		self.execute("sh %s.sh ./%s" % (test, self.user_exe), "user_output", required_files=[self.user_exe, "%s.sh" % test], trace_cmd=False, trace_output=False, maxtime=uto)	
		#self.execute("sh %s.sh ./%s" % (test, self.ref_exe), "ref_output", required_files=[self.ref_exe, "%s.sh" % test], trace_cmd=False, trace_output=False, maxtime=rto)	
		if self.diff("user_output", "%s.output" % test):
			self.comment("OK")
			self.set_grade(self.env['potential_grade'])
		else:
			self.comment("KO")

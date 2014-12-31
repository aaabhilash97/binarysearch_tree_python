class tree:
	def __init__(self,data):
		self.data=data
		self.count=1
		self.left=None
		self.right=None
	def add(self,new):
		
		if self.data==new.data:
			self.count+=1
		if self.data>new.data:
			if self.left==None:
				self.left=new
			else:
				self.left.add(new)
		if self.data<new.data:
                        if self.right==None:
                                self.right=new
                        else:
                                self.right.add(new)
	def printtree(self):
		if self!=None:
			if self.left!=None:
				self.left.printtree()
			print self.data
			if self.right!=None:
				self.right.printtree()
	def printpostorder(self):
		if self!=None:
			if self.left!=None:
				self.left.printpostorder()
			if self.right!=None:
				self.right.printpostorder()
			print self.data
	def printpreorder(self):
		if self!=None:
			print self.data
			if self.left!=None:
				self.left.printpreorder()
			if self.right!=None:
				self.right.printpreorder()
	def size(self):
		s=0
		if self!=None:
			s=1
		if self.left!=None:
			s=s+self.left.size()
		if self.right!=None:
			s=s+self.right.size()
		return s
	def buildlist(self,l):
		if type(l)==list:
			for x in l:
				self.add(tree(x))
	def maxdepth(self):
		if self==None:
			return 0
		else:
			ld=0
			rd=0
			if self.left!=None:
				ld=self.left.maxdepth()
			if self.right!=None:
				rd=self.right.maxdepth()
			if ld>rd:return ld+1
			else: return rd+1
	def minvalue(self):
		a=self
		mini=self.data
		while a!=None:
			if a.data<mini:
				mini=a.data
			a=a.left
		return mini
	def haspathsum(self):
		l=0
		r=0
		if self.left!=None:
			l=self.left.haspathsum()
		if self.right!=None:
			r=self.right.haspathsum()
		return self.data+l+r
	def printpaths(self,p=[]):
		d=self.data
		p.append(d)
		cop=[]
		for x in p:
			cop.append(x)
		if self.left==None and self.right==None:
			print p
		if self.left!=None:
			self.left.printpaths(p)
			p=cop
		if self.right!=None:
			self.right.printpaths(p)
			p=cop
	def mirror(self):
		if self.left!=None or self.right!=None:
			tmp=self.left
			self.left=self.right
			self.right=tmp
			if self.left!=None:
				self.left.mirror()
			if self.right!=None:
				self.right.mirror()
	def doubletree(self):
		if self.left!=None:
			self.left.doubletree()
		if self.right!=None:
			self.right.doubletree()
		new=tree(self.data)
		old=self.left
		self.left=new
		new.left=old
	def sametree(self,other):
		if self.left==self.right==other.right==other.left==None:
			return True
		if self.left!=None and other.left!=None:
			cond=self.left.sametree(other.left)
			if cond==False:
				return False
		elif self.left==other.left==None:
			cond=True
		else: return False
		if self.right!=None and other.right!=None:
                        cond=self.right.sametree(other.right)
			if cond==False:
				return False
                elif self.right==other.right==None:
                        cond=True
                else: return False
		return True
		
a=tree(2)
a.buildlist([1,3])
b=tree(5)
b.buildlist([4,7])
print a.sametree(b)

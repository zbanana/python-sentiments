import nltk

class Analyzer():
	"""Implements sentiment analysis."""

	def __init__(self, positives, negatives):
		"""Initialize Analyzer."""
		self.positives = []
		self.negatives = []
		pfile = open(positives, "r")
		for line in pfile:
			if line[0] != ";":
				self.positives.append(line.rstrip())
		pfile.close()
		nfile = open(negatives, "r")
		for line in nfile:
			if line[0] != ";":
				self.negatives.append(line.rstrip())
		nfile.close()

	def analyze(self, text):
		score = 0
		text = text.lower()
		# Analyze text for sentiment, returning its score
		tokens = nltk.word_tokenize(text)
		for token in tokens:
			if token in self.positives:
				score += 1
			elif token in self.negatives:
				score -= 1	
		return score

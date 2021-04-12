class LogicalAgent():

    def __init__(self,KB):
        self.KB = KB
        self.askable_atoms = [a.atom for in KB.askables]

    # TODO
    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB

        Returns:
            A list with all the logical consequences of KB
        '''
        C = []

        for ask in self.KB.askables:
            if ask not in C:
                x = True if input(f'atom {ask.atom} is true (y or n)? ') == 'y' else False

                if x:
                    C.append(ask.atom)

        while True:
            select = False
            for clause in self.KB.clauses:
                if clause.head not in C and (all(map(lambda x: x in C, clause.body))):
                    C.append(clause.head)
                    select = True
            if select == False:
                break
        return C

    # TODO
    def top_down(self,query):
               '''Implements the top down proof strategy. Given a query (the atom that it wants to prove)
        it returns True if the query is a consequence of the knowledge base.

        Args:
            querry: The atom that should be proved
        Returns:
            True if the query is a logical consequence of KB, False otherwise
        '''
        to_prove = query

        while to_prove != []:
            findClause = False

            for statement in self.KB.statements:
                if isinstance(statement, Clause):
                    if statement.head == to_prove[0]:
                        to_prove.pop(0)
                        to_prove = statement.body + to_prove
                        findClause = True
                        break

                if isinstance(statement, Askable):
                    if statement.atom == to_prove[0]:
                        x = True if input(f'atom {statement.atom} is true (y or n)? ') == 'y' else False
                        if x:
                            to_prove.pop(0)
                            findClause = True
                            break

            if findClause == False:
                return False

        return True
    
    # TODO
    def explain(self, g, explanation = set()):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.

        Args:
            g: A set of atoms that should be explained
        
        Returns:
            A list of explanation for the atoms in g
        '''
        if g:
            selected = g[0]
            if selected in self.KB.askables:
                if self.ask_askable(selected):
                    return self.explain(g[1:], explanation)
                else:
                    return []
            elif selected in self.KB.assumables:
                return self.explain(g[1:], explanation | {selected})
            else:
                l = []
                for clause in self.KB.clauses_for_atom(selected):
                    l = l + self.explain(clause.body + g[1:], explanation)

                return l
        else:
            return [explanation]

    def yes(ans):
        """ Returns true if answer is yes
        """
        return ans.lower() in ['sim','s','yes','y']

    def ask_askable(atom):
        """ Asks if atom is true
        """
        return input('Is {} true?'.format(atom))
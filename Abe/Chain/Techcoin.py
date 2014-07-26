# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X13Chain import X13Chain
from .PpcPosChain import PpcPosChain

class Techcoin(X13Chain, PpcPosChain):
    def __init__(chain, **kwargs):
        chain.name = 'Techcoin'
        chain.code3 = 'TECH'
        chain.address_version = '\x41'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xa1\xa0\xa2\xa3'
#        datadir_conf_file_name = 'Techcoin.conf'
        X13Chain.__init__(chain, **kwargs)
        

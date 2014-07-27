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

from . import BaseChain

class X15Chain(BaseChain):
    """
    A blockchain that hashes block headers using the X15 algorithm.
    The current implementation requires the bitblock_hash module.
    https://github.com/bitblockproject/bitblock_hash
    """

    def block_header_hash(chain, header):
        import bitblock_hash
        return bitblock_hash.getPoWHash(header)

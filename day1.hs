-- Advent of code 2018 day 1 challenge in haskell
-- by Antti Auranen
import Text.Printf
import Text.Read
import Control.Monad
import Data.Maybe


main = do
	line <- getLine
	let i :: Int
		i = read line
	eval <- replicateM i readLn

	
	
	
eval :: [String] -> Maybe Int
eval x = do
 	printf (fmap sum $ sequence $ x)

for i in $@
do
        koji save_failed_tree $i
done

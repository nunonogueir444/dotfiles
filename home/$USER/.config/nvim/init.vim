set mouse=a                 " enable mouse usage (all modes)
set clipboard+=unnamedplus   " enable clipboard

"let mapleader = " "

set number                 " column number
set relativenumber          " column relative numbers (num + j/k)
set nu                      " show line number when relativenumber 

set hidden                  " hide buffers when they are abandoned

syntax on
filetype plugin on        " enable syntax highlighting for many program

set nowrap                  " no wraping text allowed 

set termguicolors           " set true color

set scrolloff=10	    " cursor stay away when scrolling
set colorcolumn=80          " add warning line at x
set signcolumn=yes          " set clipboard=unnamedplus

set title
set path+=**

set nocompatible

" set expandtab
set smartindent

set showcmd
set showmode

set incsearch
set smartcase
set ignorecase

set encoding=utf-8

set dictionary=en
set complete+=kspell "????????????
set completeopt=menuone,longest "???????????



" #############################################################################
" PLUGINS #####################################################################
call plug#begin('~/.local/share/nvim/plugged')
"call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plug 'junegunn/vim-easy-align'

" Any valid git URL is allowed
Plug 'https://github.com/junegunn/vim-github-dashboard.git'

" Multiple Plug commands can be written in a single line using | separators
Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

" On-demand loading
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

" Using a non-default branch
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }

" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plug 'fatih/vim-go', { 'tag': '*' }

" Plugin options
Plug 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim' }

" Plugin outside ~/.vim/plugged with post-update hook
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
 
" MY PLUGINS ##################################################################
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Plug 'powerline/powerline-fonts'
Plug 'morhetz/gruvbox-contrib'
Plug 'morhetz/gruvbox'
"Plug 'NTBBloodbath/galaxyline.nvim'
"
"Plug 'Xuyuanp/scrollbar.nvim'
"
Plug 'ap/vim-css-color'

Plug 'vifm/vifm.vim'

Plug 'vim-scripts/AutoComplPop'

" Initialize plugin system
call plug#end()
" #############################################################################
" #############################################################################

" AIRLINE Customize the status line
set laststatus=2 "Always display the status bar
let g:airline_theme='powerlineish'
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled=1

" GRUVBOX
let g:gruvbox_termcolors = '256'
let g:gruvbox_contrast_dark = 'hard'
colorscheme gruvbox
highlight Normal guibg=NONE
